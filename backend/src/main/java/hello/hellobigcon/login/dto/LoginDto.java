package hello.hellobigcon.login.dto;

import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class LoginDto {

    private String name;
    private String email;

}
