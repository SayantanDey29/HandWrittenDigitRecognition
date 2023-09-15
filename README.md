<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Handwritten Digit Recognition Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 1);
        }
        h1 {
            font-size: 40px;
        }
        .container h1 {
            font-size: 30px;
            color:#f5f5f5;
            border-radius: 50%;
            background-color: rgb(9, 9, 107);
            text-align: center;
        } 
        .container h2 {
            color:#f5f5f5;
            background-color: rgb(61, 20, 131);
        } 
        p {
            font-size: 16px;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }
    </style>
</head>
<body>
    <header>
        <h1>Handwritten Digit Recognition Project</h1>
    </header>
    <div class="container">
        <h1>Project Description</h1>
        <h2>Overview:</h2>
        <p>
            In this project, I have developed a deep learning model based on convolutional neural networks (CNN) to excel at predicting numeric values within the range of 0 to 9 from handwritten digit images. We have also crafted a user-friendly web application using Streamlit, enabling users to upload images in JPG or PNG formats and receive accurate predictions from our model. To ensure easy access for users, we have deployed the web app on Streamlit Cloud.
        </p>
        <h2>Objective:</h2>
        <p>
            The primary objective of this project is to create a robust and user-friendly solution for handwritten digit recognition. Handwritten digit recognition has numerous real-world applications, including digitizing handwritten documents and improving accessibility for visually impaired individuals.
        </p>
        <h2>Key Components:</h2>
        <h3>Convolutional Neural Network Model:</h3>
        <p>
            <ul>
                <li>I trained a CNN model using a dataset of handwritten digits.</li>
                <li>The model consists of multiple convolutional layers, followed by max-pooling and fully connected layers.</li>
            </ul>
        </p>
        <h3>Streamlit Web Application:</h3>
        <p>
            <ul>
                <li>I designed a web application using Streamlit, a Python library for creating interactive web interfaces.</li>
                <li>The app allows users to upload images containing handwritten digits in JPG or PNG formats.</li>
                <li>Users can submit their images to the model for predictions.</li>
            </ul>
        </p>
        <h3>Deployment on Streamlit Cloud:</h3>
        <p>
            <ul>
                <li>To ensure convenient access for users, we deployed the web app on Streamlit Cloud, a platform that simplifies the deployment of Streamlit apps.</li>
                <li>This cloud deployment allows users to access the application from any web browser without the need for local setup.</li>
            </ul>
        </p>
        <img src="pic1.png" alt="Project App Screenshot">
        <h2>How it Works:</h2>
        <p>
            <ol>
                <li>Step 1: Users access the web app hosted on Streamlit Cloud.</li>
                <li>Step 2: They are presented with an intuitive interface that includes the option to upload an image containing a handwritten digit.</li>
                <li>Step 3: Users select an image and upload it to the app.</li>
                <li>Step 4: The app pre-processes the image, feeding it into the trained CNN model for prediction.</li>
                <li>Step 5: The model predicts the handwritten digit, and the result is displayed to the user along with a confidence score.</li>
                <li>Step 6: Users can easily reset the app for additional predictions or try different images.</li>
            </ol>
        </p>
        <img src="pic2.png" alt="Project App Screenshot">
        <img src="pic3.png" alt="Project App Screenshot">
        <h2>Benefits:</h2>
        <h3>User-Friendly Interface:</h3>
        <p>
            <ul>
                <li>The Streamlit-based web app offers an easy-to-use interface for users of all backgrounds.</li>
            </ul>
        </p>
        <h3>Accessibility:</h3>
        <p>
            <ul>
                <li>This application can assist visually impaired individuals in reading handwritten digits.</li>
            </ul>
        </p>
        <h3>Convenient Cloud Deployment:</h3>
        <p>
            <ul>
                <li>Hosting the app on Streamlit Cloud ensures that users can access it from anywhere with an internet connection.</li>
            </ul>
        </p>
        <h2>Conclusion:</h2>
        <p>
            My Handwritten Digit Recognition Web App is a valuable tool for various applications that require automated digit recognition. It combines the power of deep learning with the convenience of a user-friendly web interface, making it accessible to a wide range of users. Deployed on the Streamlit Cloud, it offers seamless access and demonstrates the potential of AI and machine learning in solving real-world problems.
        </p>
    </div>
</body>
</html>
