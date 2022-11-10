pipeline {

    agent any

    stages{
        stage('build'){
        
            steps{
                echo 'building the app'
            }   
        }
        stage("test_branch"){
            when{
                expression {
                        BRANCH_NAME == "python"
                }   
            }
            steps{
                 sh 'python git_webhook.py'
            }
        }
        stage('test'){
        
            steps{
                echo 'testing the app'
            }
        }
        }
    }
}
