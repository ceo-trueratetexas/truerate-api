
# TrueRate Texas – GPT-4 Property Tax Protest Platform

TrueRate Texas is an AI-powered assistant (Tex) designed to help homeowners across Texas streamline their property tax protests. The platform automates document preparation, generates persuasive protest letters, and integrates with MongoDB, Mailgun, and Stripe.

---

## Features

- GPT-4 generated protest documentation
- Integration with MongoDB Atlas for structured data storage
- Mailgun for sending PDF documentation
- Stripe for payments and promo code validation
- REST API built with Flask
- Deployable on Render with CI/CD via GitHub Actions

---

## Deployment Options

### Local Setup

1. Clone the repo:
```bash
git clone https://github.com/yourusername/truerate-texas-api.git
cd truerate-texas-api
```

2. Create a `.env` file:
```env
OPENAI_API_KEY=your-openai-api-key
MODEL_NAME=gpt-4
MAILGUN_API_KEY=your-mailgun-api-key
MAILGUN_DOMAIN=sandboxXXXX.mailgun.org
STRIPE_SECRET_KEY=your-stripe-key
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/?retryWrites=true
MONGO_DB=your-db
COLLECTIONS=sample_mflix.comments,sample_mflix.sessions,sample_mflix.users
```

3. Install dependencies:
```bash
pip install -r requirements_full.txt
```

4. Run the app:
```bash
python app_openai_gpt4.py
```

---

### Render Deployment

- Deploy using `render.yaml` or follow instructions at [Render.com](https://render.com)
- Set environment variables in the Render dashboard
- Use the CI/CD GitHub workflow to auto-deploy on push

---

## Testing the API

Run the test script:
```bash
python test_openai_generate.py
```

This sends a test prompt to `/generate`.

---

## Files Included

- `app_openai_gpt4.py`: GPT-4 API-powered backend
- `requirements_full.txt`: Dependency list
- `render.yaml`: Render deployment config
- `.github/workflows/render_deploy.yaml`: CI/CD GitHub Actions workflow
- `TrueRate_Pitch_Deck_Final_With_Charts.pptx`: Investor pitch deck
- `test_openai_generate.py`: Endpoint test script
