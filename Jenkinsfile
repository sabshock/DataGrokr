pipeline {

    agent any

    Stages('build'){
        
        steps{
                echo 'building the app'
                py start.py
        }
    }
    Stages('test'){
        
        steps{
                echo 'testing the app'
        }
    }
    Stages('deploy'){
        
        steps{
                echo 'deploy the app'
        }
    }
}