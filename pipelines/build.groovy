#!groovy

node() {
	stage ('Checkout') {
	    // the data for sample and csv was incorrect
	    deleteDir()
	    checkout scm
	}


	stage ('Executing build') {
		docker.image('python:rc-slim').inside() {
		    sh 'python src/text-to-csv.py'
		}
	}

	stage ('Release') {
	    dir('resources') {
            archiveArtifacts artifacts: '*csv', fingerprint: true
        }
	    // echo "Current workspace is $WORKSPACE"
	}
}