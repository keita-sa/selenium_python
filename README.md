[__fixture__](https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended) 


[__conftest__](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files)\
The `conftest.py` file serves as a means of providing fixtures for an entire directory. Fixtures defined in a `conftest.py` can be used by any test in that package without needing to import them (pytest will automatically discover them).

You can have multiple nested directories/packages containing your tests, and each directory can have its own `conftest.py` with its own fixtures, adding on to the ones provided by the `conftest.py` files in parent directories.

[__parametrization__](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions)
The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function.


## References

Shyshkin Dmitry. _Selenium WebDriver: Selenium Automation Testing with Python_. Udemy
