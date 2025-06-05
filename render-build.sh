#!/usr/bin/env bash

# Setup Rust properly in writable paths
export CARGO_HOME=/opt/render/project/.cargo
export RUSTUP_HOME=/opt/render/project/.rustup

# Install Rust toolchain
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $CARGO_HOME/env
rustup default stable

# Now install Python deps (this will use maturin/cargo)
pip install .
