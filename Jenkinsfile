pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "anithavalluri/python-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Checking out code from GitHub...'
                git branch: 'main', url: 'https://github.com/anithavalluri02/python1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📥 Installing Python dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r src/requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests... (add pytest later)'
                sh 'echo "No tests yet, add pytest later"'
            }
        }

        stage('Build Docker Image') {
