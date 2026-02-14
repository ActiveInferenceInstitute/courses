# Test Structure and Testing Processes

## Test Organization

### Test File Structure

Test files mirror the source code structure:

```
tests/
├── test_imports.py                    # Comprehensive import verification tests
├── test_dependencies.py               # Dependency availability and version tests
├── test_real_implementations.py       # Real implementation verification tests
├── test_markdown_to_pdf.py
├── test_text_to_speech.py
├── test_format_conversion.py
├── test_module_organization.py
├── test_canvas_integration.py
├── test_file_validation.py
├── test_integration.py
└── test_utils.py
```

### Test Function Naming

- Format: `test_[function_name]_[scenario]`
- Example: `test_render_markdown_to_pdf_success()`
- Example: `test_render_markdown_to_pdf_invalid_input()`

## Testing Processes

### Unit Testing

**Purpose**: Test individual functions in isolation

**Structure**:
```python
def test_function_name_scenario():
    # Arrange: Set up test data
    # Act: Execute function
    # Assert: Verify results
```

**Coverage**: All public functions should have unit tests

### Integration Testing

**Purpose**: Test interactions between modules

**Location**: `test_integration.py`

**Focus Areas**:
- Module interactions
- End-to-end workflows
- Error handling across modules

### Test Data Management

**Fixtures**: Use pytest fixtures for reusable test data
**Location**: `conftest.py` for shared fixtures

**Test Files**: Store test data files in `tests/data/` directory

## Test Execution

### Running Tests

**Important**: Always use `uv run pytest` to ensure tests run in the correct environment.

**All Tests**:
```bash
uv run pytest tests/
```

**Specific Module**:
```bash
uv run pytest tests/test_[module_name].py
```

**With Verbose Output**:
```bash
uv run pytest -v tests/
```

**With Coverage**:
```bash
uv run pytest --cov=src --cov-report=html tests/
```

**Import Verification**:
```bash
uv run pytest tests/test_imports.py -v
```

**Dependency Verification**:
```bash
uv run pytest tests/test_dependencies.py -v
```

**Real Implementation Verification**:
```bash
uv run pytest tests/test_real_implementations.py -v
```

### Continuous Integration

Tests should run automatically on:
- Pull requests
- Commits to main branch
- Scheduled runs

## Test Quality Standards

### Coverage Targets
- Overall coverage: > 80%
- Critical functions: > 90%
- Utility functions: > 70%

### Test Quality
- Clear test names describing scenario
- Isolated tests (no dependencies between tests)
- Fast execution (< 1 second per test)
- Deterministic results (no flaky tests)

### Documentation
- Test functions include docstrings explaining purpose
- Complex test scenarios documented
- Edge cases explicitly tested

## Real Methods Policy

### Core Principle
**All tests use real methods and implementations - no mocks, stubs, or fake methods.**

### Real Implementations
- All file operations use real file system operations
- All library calls use real library implementations (gTTS, weasyprint, etc.)
- All validation logic uses real validation functions
- All module operations use real module creation and validation

### External API Testing
- For external APIs (e.g., Canvas API), tests validate the logic and structure validation
- Tests verify that validation works correctly before API calls
- Actual API integration is tested in integration environments with real credentials
- Tests focus on the real validation and error handling logic

### Test Isolation
- Each test should be independent
- No shared state between tests
- Clean up test artifacts
- Use temporary directories for file operations

## Test Maintenance

### Regular Tasks
- Review test coverage reports
- Update tests when functions change
- Remove obsolete tests
- Refactor duplicate test code

### Validation
- All tests pass before merging
- Coverage targets maintained
- Test execution time monitored
- Flaky tests identified and fixed
