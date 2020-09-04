#!groovy

node() {
	stage ('Checkout') {
	    // the data for sample and csv was incorrect clear workspace
	    deleteDir()
		def inputFile = input message: 'Upload file', parameters: [file(name: 'sample-2.txt')]
        new hudson.FilePath(new File("$workspace/resources/sample-2.txt")).copyFrom(inputFile)
        inputFile.delete()
	    checkout scm
	}


	stage ('Executing build') {
		docker.image('python:rc-slim').inside() {
		    sh 'python src/text-to-csv.py'
		}
	}

	// stage ('Release') {
	//     dir('resources') {
	//         // Getting desired result as artifacts
    //         archiveArtifacts artifacts: '*csv', fingerprint: true
    //     }
	//     // echo "Current workspace is $WORKSPACE"
	// }
}