#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/lachlan/catkin_ws/src/fetch_ros/fetch_calibration"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/lachlan/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/lachlan/catkin_ws/install/lib/python2.7/dist-packages:/home/lachlan/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/lachlan/catkin_ws/build" \
    "/usr/bin/python2" \
    "/home/lachlan/catkin_ws/src/fetch_ros/fetch_calibration/setup.py" \
     \
    build --build-base "/home/lachlan/catkin_ws/build/fetch_ros/fetch_calibration" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/lachlan/catkin_ws/install" --install-scripts="/home/lachlan/catkin_ws/install/bin"
