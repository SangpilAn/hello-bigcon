package hello.hellobigcon.security.handler;

import com.fasterxml.jackson.databind.ObjectMapper;
import hello.hellobigcon.common.jwt.JwtTokenProvider;
import hello.hellobigcon.login.dto.LoginDto;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.Authentication;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.security.web.authentication.SimpleUrlAuthenticationSuccessHandler;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.HashMap;

@Component
@RequiredArgsConstructor
public class OAuth2LoginSuccessHandler extends SimpleUrlAuthenticationSuccessHandler {

    private final JwtTokenProvider jwtTokenProvider;
    private final ObjectMapper objectMapper;

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException {
        OAuth2User oAuth2User = (OAuth2User) authentication.getPrincipal();
        String email = oAuth2User.getAttribute("email");
        String name = oAuth2User.getAttribute("name");

        // TODO 최초 로그인 사용자 정보 DB 저장
        //  기존 사용자는 업데이트

        String token = jwtTokenProvider.createToken(email);

        LoginDto loginDto = LoginDto.builder()
                .name(name)
                .email(email)
                .build();

        HashMap<String, Object> responseData = new HashMap<>();
        responseData.put("token", token);
        responseData.put("user", loginDto);

        response.setStatus(HttpServletResponse.SC_OK);
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        objectMapper.writeValue(response.getWriter(), responseData);
    }

}
