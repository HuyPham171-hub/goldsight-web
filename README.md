# GoldSight - AI-Powered Gold Price Prediction

![Gold Price Prediction](assets/banner.png)

## 📊 Giới thiệu

**GoldSight** là một ứng dụng web interactive sử dụng Machine Learning để dự đoán giá vàng. Dự án phân tích 19.5 năm dữ liệu lịch sử (2006-2025) với 13+ chỉ số kinh tế để tạo ra các dự đoán chính xác.

### ✨ Tính năng chính

- 📈 **Data Collection**: Hiển thị các nguồn dữ liệu và phương pháp thu thập
- 🔍 **Exploratory Data Analysis (EDA)**: Phân tích tương quan, phân phối và insights
- 🤖 **Model Training**: So sánh các mô hình ML (ARIMA, LSTM, Random Forest, etc.)
- 🎯 **Forecast**: Công cụ dự đoán giá vàng real-time

## 🚀 Cài đặt và Chạy Local

### Yêu cầu hệ thống

- Python 3.11+
- Node.js 18+ (Reflex cần Node để compile frontend)
- 4GB RAM minimum

### Các bước cài đặt

1. **Clone repository**
```bash
git clone https://github.com/your-username/GoldSight-Reflex-GUI.git
cd GoldSight-Reflex-GUI
```

2. **Tạo môi trường ảo Python**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Cài đặt dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Khởi tạo Reflex**
```bash
reflex init
```

5. **Chạy ứng dụng**
```bash
reflex run
```

Ứng dụng sẽ chạy tại: `http://localhost:3000`

## 📦 Deploy lên Render.com

### Cách 1: Deploy qua GitHub (Khuyến nghị)

1. Push code lên GitHub repository của bạn
2. Đăng nhập [Render.com](https://render.com)
3. Nhấn **New** → **Web Service**
4. Kết nối GitHub repository
5. Render sẽ tự động đọc `render.yaml` và deploy

### Cách 2: Deploy thủ công

1. Tạo **New Web Service** trên Render
2. Điền thông tin:
   - **Name**: `goldsight-reflex-gui`
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt && reflex init && reflex export --frontend-only
     ```
   - **Start Command**: 
     ```bash
     reflex run --env prod --backend-only
     ```
3. Nhấn **Create Web Service**

## 🛠️ Cấu trúc dự án

```
GoldSight-Reflex-GUI/
├── goldsight/                  # Main application
│   ├── components/            # UI components (navbar, buttons, cards)
│   ├── pages/                 # Các trang (home, eda, modeling, forecast)
│   ├── services/              # Business logic (data collector, forecast)
│   ├── utils/                 # Utilities (design system, plot utils)
│   └── data/cache/            # Cached Plotly charts (JSON)
├── assets/                    # Static files (images, icons)
├── requirements.txt           # Python dependencies
├── rxconfig.py               # Reflex configuration
├── render.yaml               # Render deploy config
└── README.md                 # Documentation
```

## 📊 Công nghệ sử dụng

- **Frontend**: Reflex (Python → React)
- **Backend**: Reflex (FastAPI)
- **ML Libraries**: scikit-learn, statsmodels, TensorFlow/Keras
- **Data Processing**: pandas, numpy
- **Visualization**: Plotly, matplotlib, seaborn
- **Deployment**: Render.com

## 📈 Dataset

Dự án sử dụng 13 features chính:

**Target Variable:**
- Gold Spot Price (USD)

**Financial Markets (4):**
- S&P 500, VIX, Crude Oil, USD Index

**Macroeconomic (5):**
- CPI, Unemployment, Treasury Yield 10Y, Real Interest Rate, Fed Funds Rate

**Geopolitical (2):**
- GPR (Geopolitical Risk), GPRA (Geopolitical Risk Acts)

**Precious Metals (1):**
- Silver Futures

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

- **Huy Pham** - Greenwich University - COMP1682 Final Project

## 🔗 Links

- [Live Demo](https://goldsight-reflex-gui.onrender.com) *(thêm link sau khi deploy)*
- [GitHub Repository](https://github.com/HuyPham171-hub/gold-price-prediction)
- [Documentation](docs/)