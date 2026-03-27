#!/bin/bash
set -euo pipefail

main() {
    dx-download-all-inputs --parallel   # downloads into ~/in/<input_name>/... :contentReference[oaicite:3]{index=3}

    pushd "$HOME/in/input_rocrate"
    mkdir -p "$HOME/out/input_rocrate"
    tar -zxf "${input_rocrate_path[0]}" -C "$HOME/out/input_rocrate"
    echo "Prefix: ${input_rocrate_prefix[0]}"

    if [ -v model ] ; then
      if [ -f "${model_path[0]}" ] ; then
        echo "Model file provided: ${model}"
        echo "Model path: ${model_path[0]}"
        echo "Model path prefix: ${model_prefix[0]}"
        mkdir -p "$HOME/out/model"
        tar -zxf "${model_path[0]}" -C "$HOME/out/model"
      fi
    fi
    docker load -i /{{ cookiecutter.project_slug }}.tar.gz

    image="{{cookiecutter.docker_owner}}/{{cookiecutter.project_slug}}:@@VERSION@@"

    # Run container, mounting DNAnexus in/out
    docker run --rm \
      -v "$HOME/in:/in:ro" \
      -v "$HOME/out:/out" \
      "$image" \
      -vvv \
        --input_crate "/out/input_rocrate/${input_rocrate_prefix[0]}" \
        --mode "$mode" \
        ${model:+--model /out/model/${model_prefix[0]}} \
        ${config_file:+--config_file /in/config_file/${config_file_name[0]}} \
        "/out/${input_rocrate_prefix[0]}" || true

    ecode=$?
    echo "Exit code is: $ecode"

    tar -czf "$HOME/out/${input_rocrate_prefix[0]}.tar.gz" -C "$HOME/out/${input_rocrate_prefix[0]}" .

    dx upload "$HOME/out/${input_rocrate_prefix[0]}.tar.gz" --brief > results_file_id.txt || true
    echo "file id: "
    cat results_file_id.txt || true

    dx-jobutil-add-output results_tar "$(cat results_file_id.txt)" --class file
}


