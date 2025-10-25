pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "anithavalluri/python-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                git branch: 'main', url: 'https://github.com/anithavalluri02/python1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh """
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r src/requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "No tests yet, add pytest later"'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing image to Docker Hub...'
                withDockerRegistry([credentialsId: 'anithavalluri-docker', url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh 'kubectl apply -f k8s/'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }
    }
}
