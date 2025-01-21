# Car Rental Website

This project is the first edition of a **Car Rental Website** built using Flask, MongoDB, HTML, CSS, and Bootstrap. It allows users to browse and book cars, while administrators can manage the available cars by adding or deleting them. This version provides the foundational features, with plans for a second edition in the future.

---

## Features

### User Features
- **User Registration and Login:** Users can register and log in to access the platform.
- **Browse Cars:** View a list of cars available for rent with their images and details.
- **Book a Car:** Book a car, which will then be marked as unavailable to other users.

### Admin Features
- **Manage Cars:** Admins can add new cars to the platform and delete cars as needed.

---

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/car-rental-website.git
   cd car-rental-website
   ```
2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up the database:**
   -Install MongoDB and start the MongoDB service.
   -Create a database for the project and update the configuration in run.py

---

## Technologies Used
  -**Backend:** Flask
  -**Frontend:** HTML, CSS, Bootstrap
  -**Database:** MongoDB

---

## Future Improvements (Planned for the Second Edition)
  -Add more detailed car information (e.g., pricing, availability by date).
  -Implement a user dashboard for managing bookings.
  -Enhance the admin panel with better analytics.
  -Introduce payment integration for booking.

