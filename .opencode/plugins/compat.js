export const CompatPlugin = async ({ directory }) => {
  return {
    "shell.env": async (input, output) => {
      // Set CLAUDE_PLUGIN_ROOT to the .opencode directory in the current workspace
      // This allows skills designed for Claude Code to find their scripts via the symlinks we created
      const opencodeDir = directory + "/.opencode";
      output.env.CLAUDE_PLUGIN_ROOT = opencodeDir;
    },
  };
};
