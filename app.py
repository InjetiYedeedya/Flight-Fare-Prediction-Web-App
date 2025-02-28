from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting Form Data
        source = request.form.get('Source')
        destination = request.form.get('Destination')
        date_time = request.form.get('Date')
        airline = request.form.get('Airline')
        stops = request.form.get('Stops')

        # Validation
        if not all([source, destination, date_time, airline, stops]):
            flash("All fields are required!", "danger")
            return redirect(url_for('home'))

        # Split Date and Time
        date_part, time_part = date_time.split('T')
        year, month, day = map(int, date_part.split('-'))
        hour, minute = map(int, time_part.split(':'))

        # Dummy Prediction Logic (Replace with ML Model Prediction)
        predicted_fare = (hour * 1000) + (int(stops) * 500)
        prediction = f"Predicted Fare: ₹ {predicted_fare}"

        # Prepare Data to Display
        selected_data = {
            'Source': source,
            'Destination': destination,
            'Date': f"{day}/{month}/{year}",
            'Time': f"{hour}:{minute}",
            'Airline': airline,
            'Stops': stops
        }

        # Pass Prediction and Selected Data to Template
        return render_template('index.html', pred=prediction, data=selected_data)

    except Exception as e:
        # Log Error for Debugging
        print(f"Error: {str(e)}")
        flash("An error occurred while processing your request. Please try again.", "danger")
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
