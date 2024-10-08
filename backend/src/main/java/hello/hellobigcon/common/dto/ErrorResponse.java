package hello.hellobigcon.common.dto;

import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class ErrorResponse {

    private String error;
    private String message;

}
