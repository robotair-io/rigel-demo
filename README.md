# 🐢 turtle\_draw

A ROS 2 Python package to draw random circlular paths using `turtlesim`, including a unit-tested utility to compute circular motion.

---
## 📦 Build the Package

Make sure you are inside your ROS 2 workspace (e.g., `~/ros2_ws`) and the `turtle_draw` package is located in `src/`.

```bash
cd ~/ros2_ws
colcon build --packages-select turtle_draw
source install/setup.bash
```

---

## 🧪 Run Unit Tests

To run all unit tests for the `turtle_draw` package:

```bash
colcon test --packages-select turtle_draw
colcon test-result --verbose
```
---

## 🚀 Launch the Application

To start the application using the launch file:

```bash
ros2 launch turtle_draw turtle-draw-bringup.launch.py
```

---

## 📁 Folder Structure

```
turtle_draw/
├── turtle_draw/
│   └── main.py
├── test/
│   └── test_circle_drawer.py
├── launch/
│   └── turtle-draw-bringup.launch.py
├── package.xml
├── setup.py
```

---

## 📝 Notes

* Make sure to source the workspace setup script before testing or launching:

  ```bash
  source ~/ros2_ws/install/setup.bash
  ```
---
* Before running docker compose up, you need to allow Docker containers to access your X server:
  ```
  xhost +local:docker

  ```
* Before running docker compose pull, you need to authenticate with the ghcr otherwise the docker pull fails:
  ```
  echo $GITHUB_PAT | docker login ghcr.io -u user_name --password-stdin
  ```
