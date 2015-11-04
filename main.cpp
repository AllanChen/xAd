#include <iostream>
#include "opencv2/opencv.hpp"


using namespace cv;
using namespace std;

int main( int argc, char** argv )
{
    VideoCapture vcap(0);
    if(!vcap.isOpened()){
        cout << "Error opening video stream or file" << endl;
        return -1;
    }

    int frame_width=   vcap.get(CV_CAP_PROP_FRAME_WIDTH);
    int frame_height=   vcap.get(CV_CAP_PROP_FRAME_HEIGHT);
    VideoWriter video("/Users/Allan/Desktop/out.avi",CV_FOURCC('M','J','P','G'),10, Size(frame_width,frame_height),true);

    for(;;){

        Mat frame;
        vcap >> frame;
        video.write(frame);
        imshow( "Frame", frame );
        char c = (char)waitKey(33);
        if( c == 27 ) break;
    }
    return 0;
}
