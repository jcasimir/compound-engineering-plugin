#!/bin/bash

# Iterate over each directory in ./plugins
for plugin_dir in ./plugins/*; do
    # Check if it is a directory
    if [ -d "$plugin_dir" ]; then
        # Construct the path to the plugin configuration file
        config_path="$plugin_dir/.claude-plugin/plugin.json"
        
        # Check if the configuration file exists
        if [ -f "$config_path" ]; then
            echo "Installing plugin from $config_path..."
            bunx @every-env/compound-plugin install "$config_path" --to opencode
        else
            echo "Skipping $(basename "$plugin_dir"): Config not found at $config_path"
        fi
    fi
done
