# Description:
# AdaNet phases.
# **HIGHLY EXPERIMENTAL AND SUBJECT TO CHANGE**

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

py_library(
    name = "phase",
    srcs = ["phase.py"],
    srcs_version = "PY3",
    visibility = ["//adanet/experimental:__subpackages__"],
    deps = [
        "//adanet/experimental/work_units:work_unit",
    ],
)

py_library(
    name = "train_keras_models_phase",
    srcs = ["train_keras_models_phase.py"],
    srcs_version = "PY3",
    visibility = ["//adanet/experimental:__subpackages__"],
    deps = [
        ":phase",
        "//adanet/experimental/keras:submodel",
        "//adanet/experimental/work_units:keras_trainer",
        "//adanet/experimental/work_units:work_unit",
    ],
)