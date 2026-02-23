# Contributing to LeanIX Catalog Research Marketplace

Thank you for your interest in contributing! This marketplace contains plugins for automating LeanIX catalog research and data collection.

## How to Contribute

### Adding a New Plugin

1. **Fork the repository**
   ```bash
   git clone https://github.com/vineetgoyal1/LeanIX-Catalog-Research-Marketplace.git
   cd LeanIX-Catalog-Research-Marketplace
   ```

2. **Create your plugin directory**
   ```bash
   mkdir -p plugins/your-plugin-name/.claude-plugin
   mkdir -p plugins/your-plugin-name/skills/your-plugin-name
   ```

3. **Create plugin.json**

   Create `plugins/your-plugin-name/.claude-plugin/plugin.json`:
   ```json
   {
     "name": "your-plugin-name",
     "description": "Brief description of what your plugin does",
     "version": "1.0.0",
     "author": {
       "name": "Your Name",
       "email": "your.email@example.com"
     },
     "keywords": ["keyword1", "keyword2", "keyword3"]
   }
   ```

4. **Create SKILL.md**

   Create `plugins/your-plugin-name/skills/your-plugin-name/SKILL.md` with frontmatter:
   ```markdown
   ---
   name: your-plugin-name
   description: Detailed description of when to trigger and what it does. Include specific phrases users might say to invoke this skill.
   ---

   # Your Plugin Name

   [Your skill instructions here]
   ```

5. **Create README.md**

   Create `plugins/your-plugin-name/README.md` documenting:
   - Features
   - Usage examples
   - Prerequisites
   - Output examples

6. **Update marketplace.json**

   Add your plugin to `.claude-plugin/marketplace.json` in the `plugins` array:
   ```json
   {
     "name": "your-plugin-name",
     "source": "./plugins/your-plugin-name",
     "description": "Brief description",
     "version": "1.0.0",
     "author": {
       "name": "Your Name",
       "email": "your.email@example.com"
     },
     "keywords": ["keyword1", "keyword2"]
   }
   ```

7. **Test your plugin locally**
   - Ensure SKILL.md has proper frontmatter
   - Verify skills directory structure
   - Test that instructions are clear and complete

8. **Submit a pull request**
   ```bash
   git checkout -b add-your-plugin-name
   git add .
   git commit -m "Add your-plugin-name plugin"
   git push origin add-your-plugin-name
   ```

   Open a pull request with:
   - Description of what the plugin does
   - Example usage
   - Any prerequisites or dependencies

## Plugin Structure

```
plugins/
└── your-plugin-name/
    ├── .claude-plugin/
    │   └── plugin.json          # Plugin metadata
    ├── README.md                # Plugin documentation
    └── skills/
        └── your-plugin-name/
            ├── SKILL.md         # Main skill instructions (required)
            ├── guidelines/      # Optional: Detailed guidelines
            ├── lib/             # Optional: Python/JS modules
            └── references/      # Optional: Reference documentation
```

## Best Practices

### SKILL.md

- **Clear trigger description**: Include specific phrases users might say
- **Step-by-step instructions**: Make it easy for Claude to follow
- **Examples**: Include concrete examples for better understanding
- **Dependencies**: List required tools, MCP servers, environment variables

### Guidelines

- **Comprehensive**: Cover all edge cases and validation rules
- **Examples**: Include good and bad examples
- **Decision trees**: For complex logic, provide decision trees
- **Anti-patterns**: Show what NOT to do

### Code Modules

- **Well-documented**: Clear docstrings and comments
- **Type hints**: Use type annotations in Python
- **Error handling**: Handle edge cases gracefully
- **Testing**: Include test cases when applicable

## Code of Conduct

- Be respectful and professional
- Provide constructive feedback
- Focus on improving the marketplace for everyone
- Help others learn and grow

## Questions?

- **Issues**: Open an issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Contact**: Reach out to vineet.goyal@sap.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
