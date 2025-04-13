# API-TestPilot
API-TestPilot: An AI model collaboratively trained by JunGe (Test Development Expert) and his students to generate API test cases.

### 🌟 Overview of API-TestPilot

API-TestPilot is an AI-powered model designed to generate API test cases automatically. It aims to empower software testing engineers to enhance API testing efficiency and align with AI-driven technological advancements. 

### 🎉 API-TestPilot Version News
- 🎁 2025.04.05 API-TestPilot 1.0 is officially open-sourced and released.
- 🎁 2025.04.06 API-TestPilot Version 1.1 (pending release) fixes long-text generation repetition issues. Scheduled for release on April 7 (currently in internal testing).
- 🎁 2025.04.07 API-TestPilot 1.1, released on 2025.04.07, fixes duplication issues in long text generation and is now live. Your feedback is crucial as we prepare for the development of version 1.2. Please share your questions and issues with us.

### 🚀 API-TestPilot Core Features

By providing API documentation to the model, API-TestPilot generates comprehensive test cases tailored to your API specifications.

Deployment Simplicity & Hardware Requirements
Cost-Efficient Training: Total distillation and hardware costs amount to 380 RMB,Hardware Compatibility:Smooth operation on Tesla V100 (32GB VRAM) && Theoretically compatible with 24GB VRAM GPUs (untested).

API-TestPilot evaluates and generates test cases across the following dimensions:

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404111524_01.png)

### 💡 API-TestPilot Key Notes

Comprehensive Coverage: The model generates test cases exceeding conventional requirements but may lack domain-specific business logic. Solutions:

1.Retraining is necessary and comes at a relatively low cost. For instance, the retraining expense for the API-TestPilot model amounts to 380 RMB, encompassing both hardware utilization and knowledge distillation expenses.

2.Through the framework, the specific effects can be viewed in the video at the back of this document. Both training and the framework require test development engineers to have certain technical capabilities. Of course, the use of AI technology to enhance the work efficiency of testing will also bring an exponential increase.

3.The demo code in this project is intended exclusively for evaluating its functionality. For other requirements, you will need to find solutions on your own.

4.There are 1,000 Hamlets among 1,000 software test engineers. Therefore, we look forward to your hands-on operation and experience in evaluating the API-TestPilot model, and there will be a detailed practical deployment tutorial.

### 👥 API-TestPilot Contributors

1.API-TestPilot was completed jointly by Brother Jun and his partners. The API-TestPilot model was named by **Fu Jiaxing**.The English content of readme was completed by **Zhou Song**.Other students **participated in the entire process of model evaluation and data sets** . The training and hardware preparation and deployment process are completed by the test and development brother.

2.These little friends have distilled from **. cleaning. Test model training. Test model evaluation. Full-process technologies such as test model deployment** , especially the application of Ai technology in the testing industry, are leading the industry. In order to avoid impersonation when selecting small partners, if there is a need for authenticity verification, companies can contact the test and development brother through these small partners. The test and development brother will provide a certificate, which will include the operation records of the corresponding small partners. The following is a list of contributions (in no particular order).

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404122210.png)

### 📌 API-TestPilot Deployment Guide

Environment Setup

1.Hardware: Single GPU (32GB VRAM recommended; 24GB VRAM untested).

2.Dependencies:Python 3.12.4, pip 23.3.1 (use virtual environments).

3.Clone Repository:
git clone https://github.com/walker0012025/API-TestPilot.git  

4.cd API-TestPilot  

5.Install Dependencies:pip install -r requirements.txt。

6.Download Model: Execute `python download_api_testpilot_model.py` (downloading may take time).

7.Modify the path: Open the api_testpilot_generate_case.py source code and replace the path of model_path with your actual path (generally, you don't need to change it. If you report an error, switch to the root directory find -name api-testpilot-model and find a path similar to that in the source code to replace it).

8.Generate Test Cases:python api_testpilot_generate_case.py ,start generating interface test cases (interface information has been prepared in the source code, you can view the source code and modify it yourself).

### ⚡ API-TestPilot combined with Ai execution interface testing framework enables automatic testing with interface test cases
### ⚡ Framework development and related technologies can be learned from test developer Jun Ge. The following is the platform automatically executes interface testing based on the generated test cases.

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/1743762862000.gif)

### 🙏 Thanks from API-TestPilot and Brother Jun of Test Development

1.Thank to Zhipu AI

2.Thank to modelscope
