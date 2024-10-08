package hello.hellobigcon.login.entity;

import hello.hellobigcon.common.entity.TimeEntity;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter @Setter
@Builder
@Table(name = "users")
@AllArgsConstructor
@NoArgsConstructor
public class User extends TimeEntity {

    @Id
    private String id;

    @Column(nullable = false)
    private String username;
    @Column(nullable = false)
    private String email;

    private String picture;
}
