import { AstroAuth } from "auth-astro";
import GitHub from "@auth/core/providers/github";

export const { GET, POST } = AstroAuth({
  providers: [
    GitHub({
      clientId: import.meta.env.GITHUB_CLIENT_ID,
      clientSecret: import.meta.env.GITHUB_CLIENT_SECRET,
    }),
  ],
});