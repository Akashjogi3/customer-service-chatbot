# CODETECH INTERNSHIP PROJECT REPORT

## Customer Service Chatbot Using Python

### 1. Abstract

The Customer Service Chatbot is a desktop-based application developed using Python and Tkinter. It is designed to respond to frequently asked customer questions through an interactive graphical user interface. The chatbot provides predefined responses related to order tracking, refunds, payments, account access, shipping, and customer support. It uses keyword matching and rule-based logic to identify user queries and generate suitable responses.

### 2. Introduction

Customer support plays an important role in improving customer satisfaction. Answering repeated questions manually can consume time and resources. A chatbot can help automate responses to common queries and provide users with quick access to basic information.

This project demonstrates the development of a simple customer service chatbot with a graphical interface, searchable FAQ topics, suggested questions, message timestamps, and a clear conversation option.

### 3. Objectives

- Develop a simple and interactive customer support chatbot.
- Automate responses to frequently asked questions.
- Provide an easy-to-use graphical interface.
- Demonstrate Python programming and event handling.
- Improve accessibility to common customer service information.

### 4. Technologies Used

- **Python:** Implements the chatbot logic and application functionality.
- **Tkinter:** Creates the graphical user interface.
- **Regular Expressions:** Supports text normalization and keyword matching.
- **Visual Studio Code:** Used to develop, edit, and run the application.

### 5. System Requirements

**Hardware**
- Computer or laptop.
- Keyboard and mouse.
- Sufficient memory and storage to run Python.

**Software**
- Windows, Linux, or macOS.
- Python 3.
- Visual Studio Code or another compatible code editor.

### 6. System Design and Working

The chatbot follows a rule-based processing approach.

1. The user enters a message through the input field or selects a suggested question.
2. The application receives and normalizes the message.
3. The chatbot checks the message against predefined keywords and response rules.
4. If a matching rule is found, the corresponding response is selected.
5. The response is displayed in the chat window with a timestamp.
6. If no rule matches, the chatbot displays a fallback response.

### 7. Main Features

- Interactive graphical user interface.
- Rule-based automated responses.
- FAQ search in the sidebar.
- Suggested questions for common queries.
- Message timestamps.
- Typing indicator.
- Clear conversation option.
- Enter-key and Send-button support.
- Validation to ignore empty messages.

### 8. Testing and Results

The application was tested to verify its main features.

| Test case | Expected result |
|---|---|
| Launch the application | Chatbot window opens |
| Enter a greeting | Greeting response appears |
| Ask about order tracking | Order-related response appears |
| Ask about refunds | Refund guidance appears |
| Ask about payments | Payment guidance appears |
| Select a quick question | Question is sent to the chatbot |
| Search FAQ topics | Relevant topics are displayed |
| Send an empty message | No empty message is sent |
| Clear conversation | Messages are cleared after confirmation |

The tested features worked correctly during the project testing process.

### 9. Limitations

- Responses are based on predefined rules.
- The chatbot does not use a trained machine-learning model.
- It does not access real customer orders or account information.
- It cannot process actual payments or refunds.
- Chat history is not permanently saved.
- Responses are limited to the topics defined in the program.

### 10. Future Enhancements

- Integrate natural-language processing or an AI model.
- Add a database to store conversations.
- Connect the application to an actual customer support system.
- Add multilingual support.
- Introduce user authentication and personalized assistance.

### 11. Conclusion

The Customer Service Chatbot demonstrates how Python and Tkinter can be used to create an interactive customer support application. It automates responses to common questions and provides convenient features such as searchable FAQs, suggested questions, and message timestamps. The project helped demonstrate GUI development, string processing, conditional logic, and event handling. It can be extended in the future with machine learning and database integration.

### 12. Project Screenshots

The `screenshots` folder contains screenshots of the running application, including the welcome screen, sample conversation, and FAQ search functionality.
