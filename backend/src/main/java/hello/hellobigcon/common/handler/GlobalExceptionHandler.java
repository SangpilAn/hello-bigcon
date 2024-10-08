package hello.hellobigcon.common.handler;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import java.util.HashMap;
import java.util.Map;

@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(HttpRequestMethodNotSupportedException.class)
    public ResponseEntity<Map<String, String>> handleMethodNotAllowed(HttpRequestMethodNotSupportedException ex) {
        Map<String, String> responseBody = new HashMap<>();
        responseBody.put("error", "잘못된 메소드 요청");
        responseBody.put("message", "해당 API는 " + ex.getMethod() + " 메소드를 지원하지 않습니다.");

        return new ResponseEntity<>(responseBody, HttpStatus.METHOD_NOT_ALLOWED);
    }

}
