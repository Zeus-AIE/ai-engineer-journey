"""
Lab 1: Machine Learning Model Training & Evaluation Pipeline
Mô phỏng bài toán dự đoán rủi ro tín dụng (Credit Risk Classification) theo kịch bản Ngân hàng
"""
import os
import sys
import numpy as np

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

def run_pipeline():
    print("=" * 60)
    print("🚀 BẮT ĐẦU VÒNG ĐỜI HUẤN LUYỆN MÔ HÌNH (ML LIFECYCLE)")
    print("=" * 60)

    # 1. Tạo tập dữ liệu giả lập có độ mất cân bằng (Imbalanced) như thực tế ngân hàng
    print("1. Đang khởi tạo dữ liệu giả lập (1,000 hồ sơ vay, 10 thuộc tính tài chính)...")
    X, y = make_classification(
        n_samples=1000, 
        n_features=10, 
        n_informative=7, 
        weights=[0.85, 0.15], # 85% trả nợ tốt, 15% nợ xấu
        random_state=42
    )

    # 2. Phân chia Train - Test (80% - 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print(f"• Số mẫu tập Train: {len(X_train)}")
    print(f"• Số mẫu tập Test : {len(X_test)}")

    # 3. Huấn luyện Random Forest Classifier
    print("\n2. Đang huấn luyện mô hình Random Forest...")
    clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    clf.fit(X_train, y_train)
    print(" Huấn luyện thành công!")

    # 4. Đánh giá trên tập kiểm thử
    print("\n3. Đánh giá hiệu năng mô hình:")
    y_pred = clf.predict(X_test)
    y_proba = clf.predict_proba(X_test)[:, 1]

    roc_auc = roc_auc_score(y_test, y_proba)
    cm = confusion_matrix(y_test, y_pred)

    print("-" * 60)
    print(f"• ROC-AUC Score : {roc_auc:.4f} (Độ phân tách nợ xấu)")
    print("• Ma trận nhầm lẫn (Confusion Matrix):")
    print(f"  [ True Negative: {cm[0,0]} | False Positive: {cm[0,1]} ]")
    print(f"  [ False Negative: {cm[1,0]} | True Positive : {cm[1,1]} ]")
    print("-" * 60)
    print("\nBáo cáo chi tiết (Classification Report):")
    print(classification_report(y_test, y_pred, target_names=["Khách tốt (0)", "Nợ xấu (1)"]))

    print("=" * 60)
    print("🎯 BÀI HỌC KỸ THUẬT:")
    print("Trong bài toán nợ xấu (Imbalanced Data), Accuracy cao là 'bẫy lừa'.")
    print("AI Engineer phải tập trung vào Recall của lớp nợ xấu để tránh bỏ lọt rủi ro!")
    print("=" * 60)

if __name__ == "__main__":
    run_pipeline()
