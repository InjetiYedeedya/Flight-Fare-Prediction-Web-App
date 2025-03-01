Here’s a new **README.md** file for the **Flight-Fare-Prediction-Web-App** with updated structure and deployment instructions:  

---

# **Flight Fare Prediction Web App**  

🚀 Live Demo: [Flight Fare Prediction](https://flight-fare-prediction-web-app-041a274343e8.herokuapp.com/)  

---

## **Project Overview**  
This web application predicts flight fares based on user inputs such as airline, source, destination, departure date, arrival date, and total stops. It leverages a Machine Learning model built using `scikit-learn` and is deployed using `Flask` on `Heroku`.  

---

## **Project Structure**  
The project is organized into the following key components:  
```plaintext
Flight-Fare-Prediction-Web-App/
├── app.py                # Flask app and routing logic
├── model.py              # ML model training and saving
├── best_model.pkl        # Serialized ML model
├── Data_Train.xlsx       # Training dataset
├── Test_set.xlsx         # Testing dataset
├── requirements.txt      # Required Python packages
├── Procfile              # Heroku deployment configuration
├── templates/
│   ├── index.html        # Input form for prediction
│   └── result.html       # Result display page
└── static/
    ├── css/
    │   └── style.css     # Custom styling for the web app
    └── images/
        └── new_image.png # Images used in the app
```

---

## **How It Works**  
1. User provides flight details like airline, source, destination, departure date, arrival date, and total stops.  
2. The details are sent to the backend where the pre-trained ML model processes the inputs.  
3. The model predicts the flight fare and displays the result on a separate page.  

---

## **Technologies Used**  
- **Backend**: Flask (Python)  
- **Machine Learning**: scikit-learn  
- **Frontend**: HTML, CSS (Materialize Framework)  
- **Deployment**: Heroku  

---

## **Model Training**  
1. The model is trained using the dataset `Data_Train.xlsx` which contains historical flight fare data.  
2. The model uses features like airline, source, destination, departure date, arrival date, and total stops.  
3. The best model is saved as `best_model.pkl` for prediction.  

To **train the model**, run:  
```bash
python model.py
```

---

## **Local Setup and Installation**  
1. **Clone the Repository**:  
```bash
git clone https://github.com/your-username/Flight-Fare-Prediction-Web-App.git
cd Flight-Fare-Prediction-Web-App
```

2. **Create and Activate Virtual Environment**:  
```bash
python -m venv venv
# Activate the environment
# For Windows:
venv\Scripts\activate
# For MacOS/Linux:
source venv/bin/activate
```

3. **Install Required Packages**:  
```bash
pip install -r requirements.txt
```

4. **Create the Model File**:  
```bash
python model.py
```

5. **Run the Application**:  
```bash
python app.py
```

6. **Access the App**:  
Open the browser and navigate to: (https://flight-fare-prediction-web-app-041a274343e8.herokuapp.com/)

---

## **Deployment on Heroku**  
1. **Login to Heroku**:  
```bash
heroku login
```

2. **Create a New Heroku App**:  
```bash
heroku create your-app-name
```

3. **Add Heroku Remote Repository**:  
```bash
git remote add heroku https://git.heroku.com/your-app-name.git
```

4. **Deploy to Heroku**:  
```bash
git add .
git commit -m "Initial commit"
git push heroku master
```

5. **Open the Deployed App**:  
```bash
heroku open
```

6. **View Logs** (for troubleshooting):  
```bash
heroku logs --tail
```

---

## **Screenshots**  

### **Homepage View**  
This is the homepage where users can enter flight details:  
![Homepage](https://github.com/InjetiYedeedya/Flight-Fare-Prediction-Web-App/blob/9252f7ec7cf613af20eabb296bf2b09500d3d495/images/templete%201.png)  

### **Prediction Result View**  
After entering the details, the predicted flight fare is displayed:  
![Prediction Result](https://github.com/InjetiYedeedya/Flight-Fare-Prediction-Web-App/blob/9252f7ec7cf613af20eabb296bf2b09500d3d495/images/templete%202.png)  

---

## **Live Demo**  
Check out the deployed web app here: [Flight Fare Prediction]([https://mlflightfare-prediction.herokuapp.com/](https://flight-fare-prediction-web-app-041a274343e8.herokuapp.com/))  

---

## **Future Enhancements**  
- Add support for additional input features like flight duration and number of layovers.  
- Integrate more ML models and compare their performance.  
- Enhance the frontend UI with more dynamic and responsive design.  

---

## **Contributors**  
- **INJETI YEDEEDYA** | Company: **ineurons**  

---

## **License**  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  

---

## **Contact and Support**  
For any queries or suggestions, feel free to reach out or raise an issue in this repository.  

---

## **Acknowledgments**  
- Special thanks to **ineurons** for the support and guidance.  
- [Materialize](https://materializecss.com/) for the frontend framework.  
- [Heroku](https://www.heroku.com/) for the cloud deployment platform.  

---

You can **copy and paste** this into your new `README.md` file. If you need any other modifications or details, feel free to ask! 🚀
