# HR Chatbot with Local AI Model

An AI-powered chatbot designed to handle HR-related queries, providing instant and personalized responses to common employee questions. 
This project leverages advanced natural language processing (NLP) techniques to deliver accurate and context-aware interactions, enhancing employee engagement and streamlining HR processes.

## Tools and Libraries Used

- **Python**: The core programming language used for developing the chatbot, chosen for its extensive ecosystem and support for AI development.
- **Transformers (Hugging Face)**: Utilized for implementing the pre-trained language model, enabling the chatbot to understand and generate human-like text.
- **PyTorch**: Serves as the backend framework for the Transformers library, facilitating efficient model computations.
- **NLTK (Natural Language Toolkit)**: Employed for text preprocessing tasks such as tokenization and stop-word removal.
- **Flask**: A lightweight web framework used to create a local server for handling user interactions with the chatbot.
- **SQLite**: A lightweight database system used to store user information and chat history.
- **Docker**: Used for containerizing the application, ensuring consistent environments across different platforms.
- **Google Cloud Platform (GCP)**: Used for hosting and managing the chatbot through Google Cloud Artifact Registry and Cloud Run.
- **Git**: Version control system used for tracking changes and collaborating during the development process.
- **Jupyter Notebook**: Assisted in prototyping and experimenting with different models and preprocessing techniques during the development phase.

These tools and libraries collectively contribute to the chatbot's ability to process natural language inputs, manage conversations, and provide accurate HR-related information to users.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)
- [Google Cloud Deployment](#google-cloud-deployment)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


## Features

- **Automated Responses**: Provides instant answers to common HR questions using a static dataset.
- **AI Integration**: Utilizes a pre-trained AI model (DialoGPT) for dynamic interactions.
- **Personalization**: Remembers user details to offer a personalized experience.
- **Fallback Handling**: Offers default responses for unsupported queries.


## Installation

	1. **Clone the repository**:
	   
	   git clone https://github.com/himanshu-dandle/HR_Chatbot.git
	   
	2. Navigate to the project directory:

		cd HR_Chatbot
		
	3.Create a virtual environment:
		python -m venv venv
		

	4.Activate the virtual environment:
		venv\Scripts\activate

	5.Install the required dependencies:

	pip install -r requirements.txt
  

## Usage
	1. Run the chatbot:
		python local_chatbot.py
		
	2.Interact with the chatbot:

		Ask HR-related questions, e.g., "What is the company's leave policy?"
		Request a joke: "Tell me a joke."
		Provide your name: "My name is [Your Name]."
		Inquire about remembered details: "What is my name?
		
## Docker Deployment


	1. Build the Docker Image:
				docker build --no-cache -t hr-chatbot .
	2. Run the Container:
				docker run -p 8080:8080 hr-chatbot
	3. Access the chatbot at http://localhost:8080.

## Google Cloud Deployment

	1.Set Up Google Cloud Artifact Registry:
		a) Create a Docker repository
		
			gcloud artifacts repositories create hr-chatbot-repo \
			--repository-format=docker \
			--location=us \
			--description="Docker repository for HR Chatbot"
			
	2.Authenticate Docker with GCP
		gcloud auth configure-docker us-docker.pkg.dev
		
	3.Build and Push the Docker Image:
		a) Build:
			docker build --no-cache -t us-docker.pkg.dev/potent-app-448404-d3/hr-chatbot-repo/hr-chatbot .
		b) Push
			docker push us-docker.pkg.dev/potent-app-448404-d3/hr-chatbot-repo/hr-chatbot
	4.Deploy on Google Cloud Run:
	   Deploy the container to Cloud Run via the GCP Console or CLI.



## Future Improvements

To enhance the functionality and user experience of the HR Chatbot, consider implementing the following features:

- **Integration with OpenAI's API**: Transition from the current Hugging Face model to OpenAI's API to leverage advanced language understanding and generation capabilities.
 This integration can provide more accurate and context-aware responses, improving user satisfaction. :contentReference[oaicite:0]{index=0}

- **Integration with Company Databases**: Connect the chatbot to internal HR databases to provide real-time, personalized responses based on employee data.

- **Natural Language Processing (NLP) Enhancements**: Improve the chatbot's ability to understand and process complex queries using advanced NLP techniques.

- **Multilingual Support**: Expand the chatbot's capabilities to understand and respond in multiple languages, catering to a diverse workforce.

- **Sentiment Analysis**: Implement sentiment analysis to gauge employee emotions during interactions, allowing for more empathetic and appropriate responses.

- **Learning and Development Recommendations**: Offer personalized training and development suggestions based on employee queries and profiles.

- **Enhanced Security Measures**: Implement robust security protocols to ensure the confidentiality and integrity of employee data during interactions.

## Contributing

Contributions are welcome! Please follow these steps:

1.Fork the repository.
2. Create a new branch
	git checkout -b feature/YourFeatureName
3.Commit your changes:
	git commit -m 'Add some feature'
4.Push to the branch:
	git push origin feature/YourFeatureName


## Steps to Integrate OpenAI's API:

1. Obtain API Access: Sign up for access to OpenAI's API and retrieve your API key.

2. Install OpenAI's Python Library: Ensure that your environment includes the OpenAI library. You can install it using pip:
		pip install openai

3.Update Your Chatbot Code: Modify your chatbot's code to utilize OpenAI's API for generating responses. Here's a simplified example:


			import openai

			openai.api_key = 'YOUR_API_KEY'

			def get_response(prompt):
				response = openai.Completion.create(
					engine="text-davinci-003",
					prompt=prompt,
					max_tokens=150
				)
				return response.choices[0].text.strip()
4. Test the Integration: Run your chatbot and test various queries to ensure that the responses are accurate and contextually appropriate.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Himanshu Dandle - himanshu.dandle@gmail.com

Project Link: https://github.com/himanshu-dandle/HR_Chatbot





