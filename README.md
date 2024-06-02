# Argument-Quality-Analysis-Application

****Overview****

The Argument Quality Evaluator is a web application that uses Natural Language Processing (NLP) techniques to assess and score the quality of arguments. Leveraging pre-trained language models, this tool provides users with feedback on the coherence, relevance, and persuasiveness of their arguments. The application supports both single and multiple argument evaluations, offering detailed comparisons to help users improve their argumentative skills.

****Features****

**•Single Argument Evaluation:** Submit an argument to receive a quality score and detailed feedback on its strengths and areas for improvement.

**•Multiple Argument Comparison:** Compare two arguments to determine which one is of higher quality, with individual scores and feedback for each argument.

**•Interactive Web Interface:** A user-friendly interface built with HTML, CSS, and JavaScript, allowing for seamless interaction and quick evaluations.

**•Backend Processing:** Powered by Flask, the backend handles the processing of arguments using pre-trained models from Hugging Face Transformers library.

****Technology Stack****

**•Frontend:** HTML, CSS, JavaScript

**•Backend:** Flask, Python

**•NLP Models:** Hugging Face Transformers (BERT for sequence classification)

**•Machine Learning:** PyTorch

****Dataset****

The project uses the “IBM Debater® - IBM-ArgQ-Rank-30kArgs” dataset, which includes high-quality annotated arguments. This dataset is used to fine-tune the pre-trained models to provide accurate and reliable argument quality assessments.

**Installation and Setup**

**1.Clone the repository: **
  git clone https://github.com/Sandesh816/Argument-Quality-Analysis-Application.git
  
  cd Argument-Quality-Analysis-Application

**2.Install the required dependencies:**
 pip install -r requirements.txt

**3.Download and place the pre-trained model and tokenizer in the specified directory:**
Ensure the model and tokenizer files are located in trained_model directory within the project folder.

** 4.Run the Flask script:**
  python Flask.py

**5.Open the web interface:**
   Navigate to http://127.0.0.1:5000 in your web browser to access the Argument Quality Evaluator.

**Usage**

**Single Argument Evaluation**

1.Click on the “Single Argument” button.

2.Enter your argument in the text area.

3.Click “Evaluate” to receive a quality score and feedback.

**Multiple Arguments Comparison**

1.Click on the “Multiple Arguments” button.

2.Enter the first argument in the first text area.

3.Enter the second argument in the second text area.

4.Click “Evaluate and Compare” to receive scores and feedback for both arguments, along with a comparison result.

**Contributing**

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.
