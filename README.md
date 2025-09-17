# Supply Chain Management System

A comprehensive Django-based web application for managing suppliers, products, customers, and orders. Built as a final project for the Careeria Django course.

## 🌟 Features

- **Supplier Management**: CRUD operations for supplier information
- **Product Catalog**: Complete product management with inventory tracking
- **Customer Relationship Management**: Customer database with contact details
- **Order Processing**: Full order lifecycle management (Pending → Completed → Cancelled)
- **Admin Interface**: Built-in Django admin for advanced data management
- **Responsive Design**: Modern UI that works on desktop and mobile devices
- **Search Functionality**: Quick search across all entities

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Deployment**: Render.com
- **Version Control**: Git & GitHub

## 📦 Project Structure

```
careeria-django/
├── suppliers/                 # Project root
│   ├── suppliers/            # Project settings package
│   │   ├── settings.py       # Project configuration
│   │   ├── urls.py           # Main URL routing
│   │   └── asgi.py
│   ├── app/                  # Main application
│   │   ├── models.py         # Database models
│   │   ├── views.py          # Business logic
│   │   ├── urls.py           # App URL routing
│   │   ├── tests.py          # Unit tests
│   │   └── templates/        # HTML templates
│   └── manage.py             # Django management script
├── venv/                     # Virtual environment
└── requirements.txt          # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.13+
- PostgreSQL (for production)
- Git

### Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/AndreyGOIT/careeria-django.git
   cd careeria-django/suppliers
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**

   ```bash
   # For SQLite (development)
   python manage.py migrate

   # For PostgreSQL (update settings.py with your credentials)
   # DATABASES = {
   #     'default': {
   #         'ENGINE': 'django.db.backends.postgresql',
   #         'NAME': 'your_db_name',
   #         'USER': 'your_username',
   #         'PASSWORD': 'your_password',
   #         'HOST': 'localhost',
   #         'PORT': '5432',
   #     }
   # }
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```
   Visit: http://localhost:8000

## 📋 Database Models

### Core Entities:

- **Supplier**: Company details, contact information
- **Product**: Product information, pricing, inventory
- **Customer**: Client information and contact details
- **Order**: Order tracking with status management

### Example Model:

```python
class Order(models.Model):
    ORDER_STATUS = [
        ('PND', 'Pending'),
        ('CMP', 'Completed'),
        ('CNC', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=3, choices=ORDER_STATUS, default='PND')
    order_date = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.product.unitprice
```

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Current test coverage includes:

- Model creation and validation
- View functionality
- URL routing
- Template rendering

## 🌐 Deployment

The application is deployed on Render.com:

**Live Demo**: [https://suppliers-58p6.onrender.com](https://suppliers-58p6.onrender.com)

### Deployment Features:

- Automatic deployments from GitHub
- PostgreSQL database
- WhiteNoise for static files
- Environment variable configuration

## 🎯 Usage Guide

### For Administrators:

1. Access admin panel at `/admin`
2. Manage all database entities
3. Monitor system statistics

### For Regular Users:

1. **View Suppliers**: Browse supplier list with contact details
2. **Manage Products**: Add/edit products with inventory tracking
3. **Handle Customers**: Maintain customer database
4. **Process Orders**: Track order status and history

## 📞 API Endpoints

| Endpoint      | Method | Description            |
| ------------- | ------ | ---------------------- |
| `/suppliers/` | GET    | List all suppliers     |
| `/products/`  | GET    | List all products      |
| `/customers/` | GET    | List all customers     |
| `/orders/`    | GET    | List all orders        |
| `/admin/`     | GET    | Django admin interface |

## 🔧 Configuration

Key settings in `suppliers/settings.py`:

- Database configuration
- Static files setup
- Allowed hosts
- Installed apps
- Middleware configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is developed as part of Careeria's Django course. All rights reserved.

## 👨‍💻 Author

**Andrey Erokhin**

- GitHub: [@AndreyGOIT](https://github.com/AndreyGOIT)
- Project Repository: [careeria-django](https://github.com/AndreyGOIT/careeria-django)

## 🙏 Acknowledgments

- Careeria for the excellent Django course
- Django Software Foundation for the amazing framework
- Bootstrap team for the UI components
- Render.com for deployment platform

---

**Note**: This is a learning project developed for educational purposes as part of Careeria's professional development program.
