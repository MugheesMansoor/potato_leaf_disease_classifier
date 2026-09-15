# potato_leaf_disease_classifier
 A deep learning–based model that automatically detects and classifies potato leaf diseases from images for early crop protection.
1. End-to-end Computer Vision application

Iska matlab hai poora system start se end tak tumne banaya:

Potato leaf image → ML model → Disease prediction → User ko result

Yani user potato leaf ki picture deta hai aur system predict karta hai ke leaf healthy, Early Blight, ya Late Blight hai.

2. CNN for image classification

Tumne CNN (Convolutional Neural Network) use kiya, jo images se patterns/features learn karta hai.

Example:

Leaf image input
CNN leaf ke visual features learn karta hai
Model predict karta hai:
Healthy
Early Blight
Late Blight

Multi-class classification ka matlab hai 2 se zyada categories mein prediction karna.

3. Flask web application

Tumne trained model ko sirf notebook mein nahi rakha, balki Flask web app ke through useable banaya.

Flow:

User → Upload Leaf Image → Flask → CNN Model → Prediction → Result on Web Page

HTML/CSS frontend user ko image upload karne aur prediction dekhne ka interface provide karta hai.
