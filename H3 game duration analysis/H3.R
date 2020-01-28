H3 <- read.csv2(file = "c:/users/Treyn/Desktop/H3/H3.csv", sep=",")
str(H3)
hist(H3$GD, main="Frequency of the game durations", 
     xlab="Game duration", 
     ylab="Frequency", 
     col="olivedrab3",
     breaks=12)
boxplot(H3$GD,
        main="Boxplot of the game durations",
        ylab="Game duration",
        col="olivedrab3")

boxplot(H3$GD~H3$Faction, las=2,
        main="Game duration by faction",
        ylab="Game duration",
        col=c("green", "blue", "purple", "orange", "turquoise", "pink",
              "brown", "red"))

qqnorm(H3$GD)
qqline(H3$GD)

by(H3$GD, H3$Faction, sd)
by(H3$GD, H3$Faction, mean)

by(H3$GD, H3$TP, sd)
by(H3$GD, H3$TP, mean)
H3$Faction <- relevel(H3$Faction, ref="Stronghold")

reg <- lm(GD~Faction+TP, data=H3)
summary(reg)

drop1(reg, .~., test="F")
qqnorm(resid(reg))
qqline(resid(reg))
par(ask=F)
plot(reg)