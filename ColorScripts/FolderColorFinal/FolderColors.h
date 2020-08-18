// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "Kismet/KismetSystemLibrary.h"
#include "FolderColors.generated.h"

/**
 * 
 */
UCLASS()
class FOLDERCOLORFINAL_API UFolderColors : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	UFUNCTION(BlueprintCallable, Category = "Unreal Python")
		static void SetFolderColor(FString FolderPath, FLinearColor Color);
};
