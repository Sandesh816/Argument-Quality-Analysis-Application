from flask import Flask, request, jsonify, render_template
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

model_path = "/Users/sandesh816/Developer/NLP/trained_model"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def evaluate_argument_quality(argument):
    inputs = tokenizer(argument, padding=True, truncation=True, return_tensors="pt").to(device)
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        score = outputs.logits.squeeze().cpu().numpy().item() 
    return score

# Note, I tried to use the pipeline and text generation for feedback, but the Flask.py failed to compile on my computer while importing pipeline
def provide_feedback(score):
    if score >= 0.8:
        feedback = "Your argument is of high quality. It is coherent, relevant, and persuasive. "
    elif score >= 0.5:
        feedback = "Your argument is of moderate quality. It has some good points but could be improved. Consider strengthening your logical flow and relevance."
    else:
        feedback = "Your argument is of low quality. It lacks coherence and relevance. Try to structure your argument better and provide more persuasive points."
    return feedback

def compare_arguments(score1, score2):
    if score1 > score2:
        comparison = "The first argument is better."
    elif score1 < score2:
        comparison = "The second argument is better."
    else:
        comparison = "Both arguments are of equal quality."
    return comparison

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    argument = data['argument']
    if len(argument.split()) < 2:
        return jsonify({'score': None, 'feedback': 'Please write some more for your argument to be processed.'})
    score = evaluate_argument_quality(argument)
    feedback = provide_feedback(score)
    return jsonify({'score': score, 'feedback': feedback})

@app.route('/evaluate-multiple', methods=['POST'])
def evaluate_multiple():
    data = request.json
    argument1 = data['argument1']
    argument2 = data['argument2']
    if len(argument1.split()) < 2 or len(argument2.split()) < 2:
        return jsonify({'score1': None, 'feedback1': 'Please write some more for your argument to be processed.', 'score2': None, 'feedback2': 'Please write some more for your argument to be processed.', 'comparison': None})
    
    score1 = evaluate_argument_quality(argument1)
    feedback1 = provide_feedback(score1)
    
    score2 = evaluate_argument_quality(argument2)
    feedback2 = provide_feedback(score2)
    
    comparison = compare_arguments(score1, score2)
    
    return jsonify({'score1': score1, 'feedback1': feedback1, 'score2': score2, 'feedback2': feedback2, 'comparison': comparison})

if __name__ == '__main__':
    app.run(debug=True)