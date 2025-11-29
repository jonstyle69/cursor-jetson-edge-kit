# Cursor Development Workflow

This guide explains how to effectively use Cursor IDE to develop Edge AI applications in this project.

## Philosophy: "Jetson Read" First

Before making any changes, always follow the "Jetson Read" approach:

1. **Read the requirements**: Understand what you're trying to build
2. **Read existing code**: Review related modules and examples
3. **Plan your changes**: Think about which files need modification
4. **Then code**: Let Cursor help you implement

This prevents unnecessary rewrites and ensures your changes fit the existing architecture.

## Iterative Development Process

### 1. Set the Task

Clearly define what you want to accomplish. For example:
- "Add support for MIPI camera on Jetson"
- "Integrate YOLOv8 inference with TensorRT"
- "Add frame rate monitoring to the pipeline"

### 2. Plan File Changes

Before asking Cursor to make changes, list:
- Which files will be modified
- What each file's role is in the change
- Any new files that need to be created

Example:
```
Files to modify:
- kit/camera.py: Add MIPI camera support alongside USB
- kit/config.py: Add camera source configuration
- examples/minimal_camera_pipeline.py: Update to use new config

New files:
- docs/jetson_camera_setup.md: Documentation for MIPI setup
```

### 3. Let Cursor Edit

Use Cursor's AI assistance to:
- Generate boilerplate code
- Refactor existing code
- Add type hints and docstrings
- Fix bugs and improve structure

**Pro tip**: Break large changes into smaller, focused requests. Cursor works better with specific, incremental tasks.

### 4. Run Tests

After changes:
- **On PC**: Test with `python examples/minimal_camera_pipeline.py`
- **On Jetson**: Deploy and test with real hardware
- Check for errors, performance issues, or unexpected behavior

### 5. Log Results

Document your iteration:
- What worked?
- What didn't?
- What would you do differently?
- Performance metrics (FPS, latency, etc.)

Consider maintaining a dev log (we may add a `dev_log/` directory in the future).

## Cursor Chat Best Practices

### Effective Prompts

**Good prompts:**
- "Add a `get_fps()` method to the Pipeline class that returns the current frame rate"
- "Refactor the camera initialization to support both USB and MIPI sources based on config"
- "Add type hints to all functions in `kit/inference.py`"

**Less effective prompts:**
- "Fix the code" (too vague)
- "Make it better" (no clear goal)
- "Do everything" (too broad)

### Using .cursorrules

The `.cursorrules` file guides Cursor's behavior:
- Enforces security practices (no hardcoded secrets)
- Maintains code style (type hints, modularity)
- Reminds about Git workflow

Cursor will automatically follow these rules when making suggestions.

## Example Workflow: Adding a New Feature

Let's say you want to add frame rate monitoring:

1. **Set task**: "Add FPS monitoring to the Pipeline class"

2. **Plan changes**:
   ```
   - kit/pipeline.py: Add FPS tracking logic
   - kit/config.py: Add FPS display configuration option
   - examples/minimal_camera_pipeline.py: Enable FPS display
   ```

3. **Ask Cursor**: 
   ```
   Add FPS monitoring to the Pipeline class. Track frames per second 
   and provide a method to get current FPS. Add a config option to 
   enable/disable FPS display.
   ```

4. **Review changes**: Check that Cursor's implementation:
   - Follows the existing code style
   - Has proper type hints
   - Includes docstrings
   - Doesn't break existing functionality

5. **Test**: Run the example and verify FPS is calculated correctly

6. **Document**: Update relevant docs if needed

## Git Workflow Integration

After making changes, use the semi-automated Git workflow:

```bash
bash tools/git_semi_auto.sh
```

This script will:
- Show you what changed
- Check for sensitive files
- Help you create a meaningful commit message
- Optionally push to remote

## Common Patterns

### Adding a New Module

1. Create the file in `kit/`
2. Define the class with type hints
3. Add docstrings
4. Export in `kit/__init__.py`
5. Create an example usage

### Extending Existing Functionality

1. Read the existing implementation
2. Identify extension points
3. Add new methods/parameters without breaking existing code
4. Update examples to show new features

### Debugging with Cursor

- Paste error messages into Cursor Chat
- Ask Cursor to explain the error
- Request fixes with context about your goal
- Review suggested fixes before applying

## Tips for Success

1. **Start small**: Build minimal working examples first
2. **Iterate**: Make small changes, test, then improve
3. **Document as you go**: Add docstrings and comments while coding
4. **Use Cursor's suggestions**: But always review before accepting
5. **Test frequently**: Don't wait until everything is "done"

## Next Steps

- Try modifying `examples/minimal_camera_pipeline.py`
- Add a new method to one of the `kit/` modules
- Experiment with Cursor's refactoring suggestions
- Build your own pipeline!

