package hello.hellobigcon.common.jwt.errors;

import io.jsonwebtoken.JwtException;

public class JwtLogoutException extends JwtException {
    public JwtLogoutException(String message) {
        super(message);
    }

    public JwtLogoutException(String message, Throwable cause) {
        super(message, cause);
    }
}
