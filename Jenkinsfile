pipeline {

    agent any

    stages{
        stage('build'){
        
            steps{
                echo 'building the app'
            }   
        }
        stage("test_branch"){  
            
            steps{
                 sh 'py git_webhook.py'
            }
        }
        stage('test'){
        
            steps{
                echo 'testing the app'
            }
        }
        }
    }
