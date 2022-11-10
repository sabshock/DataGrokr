pipeline {

    agent any

    stages{
        stage('build'){
        
            steps{
                echo 'building the app'
            }   
        }
        stage('test-branch'){
            when{
                branch "test"
            }
            steps{
                sh ''' 
                py git_webhook.py
                '''
            }
        }
        stage('test'){
        
            steps{
                echo 'testing the app'
            }
        }
        stage('deploy'){
        
            steps{
                echo 'deploy the app'
            }
        }
    }
}