# Movie-Review-Page


## **Setting Up the Project Locally**
1. **Clone the Repository from GitHub**
    - git clone repository-url
    - cd project-folder
2. ** Open the Project Folder**
    - cd <path-to-manage.py>.
3. **Set Up a Virtual Environment**
    - python -m venv env
    -.\env\Scripts\activate.
4. **Install the Required Packages**
    - pip install django
    -pip install Pillow.
5. **Run the Development Server**
    - python manage.py runserver
6. **Access the website**
    - http://127.0.0.1:8000

## **Features Implemented**

1. **User Authentication**
    - Register a new account.
    - Log in and log out.
    - Secure CSRF-protected forms.
2. **Dashboard**
    - Personalized dashboard for users to view and manage their reviews.
3. **Add a Review**
    - Submit a review with a movie name, rating, review description, and photo upload.
4. **Edit a Review**
    - Modify existing reviews, including updating the rating, review, and photo.
5. **Delete a Review**
    - User can delete the reviews, created by them from the Dashboard
6. **Complete Review**
    - A dedicated page Each Movie review, where user can see the complete review.
7. **Like and Comments**
    - User can like and comment the reviews, Users can see the Dynamic count of Likes and Comments in the main page.
8. **Responsive and Modern Design**
    - All pages are styled with Bootstrap for a professional and clean user experience

## **Technologies Used**

1. **Backend**: Django Framework
    - Django ORM for database management.
    - Django forms for secure input handling.
2. **Frontend**:
    - Bootstrap 4 for responsive design.
    - HTML and CSS for additional customization.
3. **Other Tools**:
    - Django templates for rendering dynamic pages

## **Limitations or Known Issues**

1. **No Email Notifications**:
    - The application lacks email notifications for registration or password resets.

## **Future Enhancements**

1. Integrate email notifications for user account actions.
2. Add analytics to display average ratings for each movie.


## **SnapShots**


1. **Registration Page**
![regpage](https://github.com/user-attachments/assets/990b327c-d454-4e6a-b509-fc7c161f2a3f)

2. **Login Page**
![Loginpahe](https://github.com/user-attachments/assets/07f4359e-97f7-4bb5-a036-2e0d62400e2d)

3. **Home Page**
![Home Page](https://github.com/user-attachments/assets/cd4201b8-75c6-4c08-b58a-b59d613bc6d3)

4. **Detail Review Page**
![page2](https://github.com/user-attachments/assets/79c30fe0-c3fc-4c24-adb3-525c5c0a93c8)

5.**User Dashboard**
![Page 3](https://github.com/user-attachments/assets/c98390c4-6769-4bd6-bd33-ca4f425b2942)

6. **Add a Review**
![page 4](https://github.com/user-attachments/assets/619986f1-d886-4659-beef-812a76295d76)

7. **Edit a Review**
![editpage](https://github.com/user-attachments/assets/5e061776-1238-49b3-b7a1-54e72d9c1991)









