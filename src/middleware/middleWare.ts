// Middleware

//Passport Auth
import { PassportModule } from '@nestjs/passport';
import { CacheModule } from '@nestjs/cache-manager';
import { Module } from '@nestjs/common';
import { Cron, CronExpression } from '@nestjs/schedule';

@Module({
  imports: [PassportModule.register({ defaultStrategy: 'local' })],
})
export class AuthModule {}

// Cache Management
@Module({
    imports: [CacheModule.register()],
  })
  export class AppModule {}

  //Chron Jobs
  @Injectable()
    export class TasksService {
    @Cron(CronExpression.EVERY_MINUTE)
    handleCron() {
        console.log('Called every minute');
    }
}