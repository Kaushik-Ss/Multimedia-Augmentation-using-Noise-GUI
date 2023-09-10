from cx_Freeze import setup, Executable

# Define the executables and their options
executables = [Executable("main.py")]

# Specify any additional files or packages that need to be included
additional_modules = [
    "imageio",
    "matplotlib",
    "numpy",
    "cv2",
    "PIL",
    "PyQt5",
    "scipy",
]

# Create the setup configuration
setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    options={
        "build_exe": {
            "packages": additional_modules,
        },
    },
    executables=executables,
)
