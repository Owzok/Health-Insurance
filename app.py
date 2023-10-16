from flaskapp import app

if __name__ == '__main__':
    app.run(debug=True)

"""
APPLIED SECURITY POLICIES
- [x] Bearer Expirable Token
- [x] Password Policies: Enforced strong password
- [x] Brute Force Protection
- [ ] HTTPS (mmm technically its done, but truly, for now it is not a good idea)
- [ ] Input Validation: XSS and SQL injection protection (pay AWS WAF)
- [x] Rate Limiting
- [x] Logging
- [x] Account Lockout
"""