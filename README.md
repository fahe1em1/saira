# Saira Telehealth Website

This repository contains a simple telehealth website implemented with vanilla Node.js. The site allows users to view basic information about the service and includes placeholder functionality for video calls.

## Running Locally

```bash
npm start --prefix telehealth
```

Then open `http://localhost:3000` in your browser.

## Running Tests

```bash
npm test --prefix telehealth
```

## Deployment

The website can be deployed on any platform that supports Node.js (e.g. Heroku, Vercel). Build steps are minimal because no external dependencies are required. Push the contents of the `telehealth` directory to your chosen provider and set the start command to `node server.js`.
