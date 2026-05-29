import { AstroAuth } from "auth-astro";
import GitHub from "@auth/core/providers/github";
// Добавь эти импорты
import { PrismaAdapter } from "@auth/prisma-adapter";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const { GET, POST } = AstroAuth({
  // Вот эта строка обязательна для auth-astro:
  adapter: PrismaAdapter(prisma), 
  providers: [
    GitHub({
      clientId: import.meta.env.GITHUB_CLIENT_ID,
      clientSecret: import.meta.env.GITHUB_CLIENT_SECRET,
    }),
  ],
});