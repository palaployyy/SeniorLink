pipeline {
    agent any
    
/////////////////////////////////////////////////////////////////////////////////////////// ENV //////////////////////////////////////////////////////////////////////////////////////
    environment {
        DOCKER_IMAGE_FRONTEND = 'earth123456789/seniorfrontend:latest'
        DOCKER_IMAGE_BACKEND = 'earth123456789/seniorbackend:latest'
        DOCKER_CREDENTIALS = credentials('dockerhub')
    }



/////////////////////////////////////////////////////////////////////////////////////////// Checkout Code (Github) //////////////////////////////////////////////////////////////////////////////////////
    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Checkout source code from repository
                    echo 'Checking out code...'
                    git url: 'https://github.com/bbiiw/SeniorLink.git', branch: 'main'
                }
            }
        }

/////////////////////////////////////////////////////////////////////////////////////////// Docker Image //////////////////////////////////////////////////////////////////////////////////////
        stage('Build Frontend Docker Image') {
            steps {
                script {
                    // Build Docker image for frontend
                    echo 'Building frontend Docker image...'
                    dir('frontend') {
                        sh 'docker build -t $DOCKER_IMAGE_FRONTEND .'
                    }
                }
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                script {
                    // Build Docker image for backend
                    echo 'Building backend Docker image...'
                    dir('backend') {
                        sh 'docker build -t $DOCKER_IMAGE_BACKEND .'
                    }
                }
            }
        }


/////////////////////////////////////////////////////////////////////////////////////////// Docker Hub //////////////////////////////////////////////////////////////////////////////////////
        
        stage('Push Frontend Docker Image to Docker Hub') {
            steps {
                script {
                    // Push frontend Docker image to Docker Hub
                    echo 'Pushing frontend Docker image to Docker Hub...'
                    sh 'echo $DOCKER_CREDENTIALS_PSW | docker login --username $DOCKER_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $DOCKER_IMAGE_FRONTEND'
                }
            }
        }

        stage('Push Backend Docker Image to Docker Hub') {
            steps {
                script {
                    // Push backend Docker image to Docker Hub
                    echo 'Pushing backend Docker image to Docker Hub...'
                    sh 'echo $DOCKER_CREDENTIALS_PSW | docker login --username $DOCKER_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $DOCKER_IMAGE_BACKEND'
                }
            }
        }

/////////////////////////////////////////////////////////////////////////////////////////// Docker Compose //////////////////////////////////////////////////////////////////////////////////////

        stage('Start Docker Compose') {
            steps {
                script {
                    // Start services using Docker Compose
                    echo 'Starting services with Docker Compose...'
                    sh 'docker-compose -f docker-compose.yml up --build -d'
                }
            }
        }
    }

/////////////////////////////////////////////////////////////////////////////////////////////// Restart Nginx หรือแจ้งให้ Nginx รู้ว่ามีบริการใหม่ ////////////////////////////////////////////////////////////////////////////////
        stage('Restart Nginx') {
            steps {
                script {
                    echo 'Restarting Nginx...'
                    sh 'sudo systemctl restart nginx'  // คุณอาจต้องแน่ใจว่า Jenkins มีสิทธิ์ในการรันคำสั่งนี้
                }
            }
        }
    }

/////////////////////////////////////////////////////////////////////////////////////////// Docker logout //////////////////////////////////////////////////////////////////////////////////////
    post {
        always {
            // Logout from Docker Hub
            sh 'docker logout'
        }
    }
}
