require 'json'
require 'yaml'
require 'fileutils'

# Helper to print status
def status(message, type = :info)
  icon = case type
         when :success then "✅"
         when :error then "❌"
         when :warning then "⚠️"
         else "ℹ️"
         end
  puts "#{icon} #{message}"
end

def fail_task(message)
  status(message, :error)
  exit 1
end

namespace :validate do
  namespace :claude do
    desc "Validate the Claude Marketplace configuration"
    task :marketplace do
      puts "\n🔍 Validating Claude Marketplace..."
      
      marketplace_path = File.join(Dir.pwd, ".claude-plugin", "marketplace.json")
      
      unless File.exist?(marketplace_path)
        # Try root location as fallback (though strictly should be in .claude-plugin)
        marketplace_path = File.join(Dir.pwd, "marketplace.json")
        unless File.exist?(marketplace_path)
          fail_task "Marketplace manifest not found at .claude-plugin/marketplace.json"
        end
      end

      begin
        data = JSON.parse(File.read(marketplace_path))
        
        # Check required fields
        required_fields = ["name", "owner", "plugins"]
        missing = required_fields - data.keys
        fail_task "Missing required fields in marketplace.json: #{missing.join(', ')}" unless missing.empty?

        status "Marketplace manifest found and valid JSON"
        
        # Validate listed plugins exist
        if data["plugins"].is_a?(Array)
          data["plugins"].each do |plugin|
            name = plugin["name"]
            source = plugin["source"]
            
            # Handle object source vs string source
            source_path = source.is_a?(Hash) ? source["source"] : source
            
            # If source is a relative local path, verify it exists
            if source.is_a?(String) && source.start_with?(".")
              full_path = File.expand_path(source, Dir.pwd)
              if Dir.exist?(full_path)
                status "Plugin '#{name}' path verified: #{source}", :success
              else
                status "Plugin '#{name}' path NOT found: #{source}", :error
                exit 1
              end
            end
          end
        else
          fail_task "'plugins' field must be an array"
        end

      rescue JSON::ParserError => e
        fail_task "Invalid JSON in marketplace.json: #{e.message}"
      end
      
      puts "\n✨ Claude Marketplace validation passed!"
    end

    desc "Validate each Claude Plugin"
    task :plugins do
      puts "\n🔍 Validating Claude Plugins..."
      
      # Discover plugins: Strategy 1 - Read marketplace.json
      plugins_dirs = []
      marketplace_path = File.join(Dir.pwd, ".claude-plugin", "marketplace.json")
      
      if File.exist?(marketplace_path)
        begin
          data = JSON.parse(File.read(marketplace_path))
          if data["plugins"].is_a?(Array)
            data["plugins"].each do |p| 
              src = p["source"]
              plugins_dirs << src if src.is_a?(String) && src.start_with?(".") && Dir.exist?(src)
            end
          end
        rescue
          # Ignore errors here, just fallback to directory scan
        end
      end
      
      # Strategy 2 - Scan plugins/ directory if empty
      if plugins_dirs.empty?
        plugins_dirs = Dir.glob("plugins/*").select { |f| File.directory?(f) }
      end
      
      fail_task "No plugins found to validate" if plugins_dirs.empty?
      
      plugins_dirs.each do |plugin_dir|
        puts "\nChecking plugin at: #{plugin_dir}"
        manifest_path = File.join(plugin_dir, ".claude-plugin", "plugin.json")
        
        unless File.exist?(manifest_path)
          status "Missing .claude-plugin/plugin.json in #{plugin_dir}", :error
          next
        end
        
        begin
          plugin_data = JSON.parse(File.read(manifest_path))
          
          # Check strict mode requirements (agents/commands/skills paths)
          components = ["agents", "commands", "skills"]
          has_component = components.any? { |c| plugin_data.key?(c) }
          
          # Verify component paths if they exist
          components.each do |comp|
            if plugin_data[comp]
              paths = Array(plugin_data[comp])
              paths.each do |path|
                # Paths in plugin.json are relative to the plugin root (where .claude-plugin/ is usually, but strictly relative to manifest location or plugin root depending on interpretation)
                # The docs say: "All paths must be relative to plugin root and start with ./"
                # Since plugin.json is in .claude-plugin/, we assume paths like "../agents/" or "./agents/" relative to plugin root
                
                # Resolving relative to plugin_dir
                resolved_path = File.expand_path(path, plugin_dir)
                
                if Dir.exist?(resolved_path) || File.exist?(resolved_path)
                  status "  Verified #{comp} path: #{path}", :success
                else
                  status "  Invalid #{comp} path: #{path} (resolved to #{resolved_path})", :error
                end
              end
            end
          end
          
          status "  Valid manifest for #{plugin_data['name']}", :success
          
        rescue JSON::ParserError
          status "  Invalid JSON in plugin.json", :error
        end
      end
    end
  end

  namespace :opencode do
    desc "Validate OpenCode Plugin compatibility"
    task :plugins do
      puts "\n🔍 Validating OpenCode Compatibility..."

      # 1. Check opencode.json
      if File.exist?("opencode.json")
        begin
          JSON.parse(File.read("opencode.json"))
          status "opencode.json exists and is valid JSON", :success
        rescue JSON::ParserError
          fail_task "opencode.json contains invalid JSON"
        end
      else
        fail_task "Missing opencode.json in root"
      end

      # 2. Check .opencode directory structure
      [".opencode/agents", ".opencode/commands", ".opencode/skills"].each do |dir|
        if Dir.exist?(dir)
          status "Directory #{dir} exists", :success
          
          # 3. Check for broken symlinks
          Dir.glob("#{dir}/*").each do |file|
            if File.symlink?(file)
              begin
                target = File.readlink(file)
                # Resolve relative symlink
                target_path = File.expand_path(target, File.dirname(file))
                
                if File.exist?(target_path)
                  # status "  Link valid: #{File.basename(file)}", :success
                else
                  status "  BROKEN LINK: #{file} -> #{target}", :error
                end
              rescue => e
                status "  Error reading link #{file}: #{e.message}", :error
              end
            end
          end
        else
          status "Directory #{dir} missing", :warning
        end
      end
      
      # 4. Check compat.js plugin
      compat_plugin = ".opencode/plugins/compat.js"
      if File.exist?(compat_plugin)
        status "Compatibility plugin found at #{compat_plugin}", :success
      else
        status "Missing compatibility plugin at #{compat_plugin}", :warning
      end

      puts "\n✨ OpenCode compatibility validation passed!"
    end
  end
end

task :default => ["validate:claude:marketplace", "validate:claude:plugins", "validate:opencode:plugins"]
