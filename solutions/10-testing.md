# Solution 10 — Testing

Add to `examples/python-app/tests/test_app.py`:

```python
def test_add_zero_zero():
    assert add(0, 0) == 0
```

Run locally with `python -m pytest`, or push to let workflow `06-test-python.yml` run it.