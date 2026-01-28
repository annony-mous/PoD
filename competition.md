# 🏁 PoD-Based Dataset Creation Competition

## Name
Dataset containing potholes in road images

## Features
- Color or Black-White: Color  
- Lighting Condition: Daylight  
- Pothole Severity: Minor, deep, and dangerous holes  
- Dataset Size: > 10  

## Statistical Measures
- Image size: Minimum 1280 × 760  
- Mean: Red – 130, Green – 140, Blue – 160 (nearly)  
- Standard deviation: Red – 18, Green – 20, Blue – 22 (nearly)  
- Skewness: No more than 0.0001  
- Kurtosis: All channels – 3.01 (nearly)  
- Pixel distribution: Relatively uniform without dominant peaks or gaps  
- SSIM: ≤ 0.9 (nearly)  
- Outliers: 0 (or 1)

## Model-based Evaluation
- Pre-trained model name: Ultralytics YOLOv8  
- Model link: https://github.com/ultralytics/ultralytics  
- Accuracy: > 90%  
- F1-score: > 85%  
- Precision and Recall: > 87%  
- Mean Squared Error (MSE): < 0.1  
