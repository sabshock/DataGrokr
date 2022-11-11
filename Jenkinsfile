pipeline {

    agent any

    environment {
        DOCKERHUB_CRED = credentials('dockerhub')
    }

    stages{
        stage('Git-checkout'){
            steps{
                echo " Checking out git Repo"
                git branch: 'python', url: 'https://github.com/sabshock/DataGrokr.git'
            }
        }
        stage('build'){
        
            steps{
                echo 'building the app'
            }   
        }
        stage("test"){
            steps{
                 bat 'py test_calc.py'
            }
        }
        stage('deploy'){
        
            steps{
                bat 'docker build -t sab10/calculator_image .'
                
            }
        }
        stage('Login'){

            steps{
                bat 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

            }
        }
        stage('Push'){

            steps{
                bat 'docker push sab10/calculator_image'
            }
        }
    }
    
    post {
        always{
            bat 'docker logout'
        }
        success{
            echo 'calculator app docker image is successfully got deloyed to docker hub'
        }

    }
}