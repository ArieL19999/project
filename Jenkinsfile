
pipeline {
    
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ArieL19999/second.git'
            }
        }
        
        stage('Build and run Image') {
            steps {
                script {
                    // env.myImage = docker.build('pnb20/on-my-own', '--build-arg ARG_NAME=ARG_VALUE -f "C:/Users/eitan/Dockerfile" --tag latest .')
                    // env.myContainer = env.myImage.run("-p 8777:8777 -v C:/Users/eitan/Scores.txt:/app/Scores.txt")
                    // println env.myContainer
                    bat "docker build --build-arg ARG_NAME=ARG_VALUE  --tag test_image ."
                    bat "docker run  -d -p 8777:8777 -v C:\\Users\\eitan\\Scores.txt:\\app\\Scores.txt --name test_run test_image"
                }
            }
        }
        
        stage('Test') {
            steps {
                bat '"C:/Program Files/Amazon/AWSCLI/runtime/python.exe" e2e.py'
            }
        }
        
        stage('Stop Docker Container') {
            steps {
                script {
                    //  docker.stop(env.myContainer.id)
                    bat "docker kill test_run"
                    bat "docker rm -f test_run "
                }
            }
        }
    }
}
